import re

with open('biosyn_agi_demo.html', 'r', encoding='utf8') as f:
    html = f.read()

# Add a global error handler to the start of <script>
error_handler = """<script>
window.onerror = function(msg, url, line, col, error) {
  var errDiv = document.createElement('div');
  errDiv.style.cssText = 'position:fixed;top:0;left:0;width:100%;background:red;color:white;padding:20px;z-index:9999;';
  errDiv.innerHTML = '<strong>JavaScript Error:</strong> ' + msg + ' (Line: ' + line + ')';
  document.body.prepend(errDiv);
};
"""

html = html.replace('<script>', error_handler)

with open('biosyn_agi_demo.html', 'w', encoding='utf8') as f:
    f.write(html)
