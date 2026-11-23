/* Pure functions shared by the interface and its regression tests. */
(() => {
  'use strict';
  const normalize = value => String(value ?? '').normalize('NFD').replace(/\p{M}/gu, '').toLocaleLowerCase();
  const escapeHTML = value => String(value ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  function wordCount(text) {
    return String(text ?? '').match(/[\p{L}\p{N}]+(?:[’'-][\p{L}\p{N}]+)*/gu)?.length ?? 0;
  }
  function readingMinutes(text) { const n = wordCount(text); return n ? Math.ceil(n / 200) : 0; }
  function bodyText(article) { return article.sections.map(s => [s.title, ...s.paragraphs].join(' ')).join(' '); }
  function highlight(text, query) {
    const value = String(text), needle = normalize(query).trim();
    if (!needle) return escapeHTML(value);
    // Keep a map to the original UTF-16 positions so accents and emoji survive.
    let folded = ''; const starts = [], ends = [];
    let offset = 0;
    for (const char of value) {
      const part = normalize(char);
      for (let j = 0; j < part.length; j++) { starts.push(offset); ends.push(offset + char.length); }
      folded += part; offset += char.length;
    }
    let cursor = 0, from = 0, out = '', at;
    while ((at = folded.indexOf(needle, from)) !== -1) {
      const start = starts[at], end = ends[at + needle.length - 1];
      out += escapeHTML(value.slice(cursor, start)) + '<mark>' + escapeHTML(value.slice(start, end)) + '</mark>';
      cursor = end; from = at + needle.length;
    }
    return out + escapeHTML(value.slice(cursor));
  }
  function matches(article, query, category) {
    if (category && category !== 'all' && article.category !== category) return false;
    const q = normalize(query).trim();
    return !q || normalize([article.title, article.excerpt, article.author, ...article.tags, bodyText(article)].join(' ')).includes(q);
  }
  function progress(top, bottom, viewportHeight) {
    const distance = bottom - top - viewportHeight;
    if (distance <= 0) return top <= 0 ? 100 : 0;
    return Math.max(0, Math.min(100, Math.round(-top / distance * 100)));
  }
  const defaults = () => ({version: 1, saved: [], theme: 'light', font: 'medium', language: 'es', comments: {}});
  function sanitizeState(raw, ids) {
    const state = defaults(), allowed = new Set(ids);
    if (!raw || typeof raw !== 'object') return state;
    state.saved = [...new Set(Array.isArray(raw.saved) ? raw.saved.filter(id => allowed.has(id)) : [])];
    for (const [key, values] of Object.entries({theme: ['light','dark','sepia'], font: ['small','medium','large'], language: ['es','en']})) {
      if (values.includes(raw[key])) state[key] = raw[key];
    }
    if (raw.comments && typeof raw.comments === 'object') {
      for (const id of ids) {
        if (!Array.isArray(raw.comments[id])) continue;
        state.comments[id] = raw.comments[id].filter(c => c && typeof c.alias === 'string' && typeof c.message === 'string' &&
          c.alias.trim().length >= 2 && c.alias.length <= 40 && c.message.trim().length > 0 && c.message.length <= 500 &&
          typeof c.date === 'string' && Number.isFinite(Date.parse(c.date))).slice(-100).map(c => ({alias:c.alias, message:c.message, date:c.date}));
      }
    }
    return state;
  }
  function validateComment(alias, message) {
    return {alias: alias.trim().length < 2 || alias.length > 40, message: message.trim().length < 1 || message.length > 500};
  }
  globalThis.PausaCore = {normalize, escapeHTML, wordCount, readingMinutes, bodyText, highlight, matches, progress, defaults, sanitizeState, validateComment};
})();
