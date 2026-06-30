// chat.js
//
// All frontend logic. Imported by index.html.
//
// Responsibilities:
//   1. Maintain `history` array in memory: [{role: "user"|"assistant", content: "..."}]
//      Reset on page load. Grows each turn. Sent with every POST.
//
//   2. sendMessage(text):
//      - Append user message to history and render it
//      - Disable input while waiting
//      - POST {message: text, history: history} to /chat
//      - Open EventSource (or use fetch + ReadableStream for SSE)
//      - Handle incoming events:
//          "token"  → append chunk to current assistant bubble
//          "status" → update status line
//          "error"  → show error, re-enable input
//          "done"   → finalize assistant message, append to history, re-enable input
//
//   3. renderMessage(role, content):
//      Creates a message bubble and appends to message area. Returns the element
//      so token chunks can be appended to it incrementally.
//
// Note on SSE with POST:
//   Native EventSource only supports GET. For POST + SSE, use fetch() with
//   response.body.getReader() and decode the stream manually.
//   This is ~20 lines and is the right approach here.
//
// No jQuery, no framework. Vanilla JS only.
