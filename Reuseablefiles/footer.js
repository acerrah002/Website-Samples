const FooterHTML = `
  <footer class="footer">
    <p>This is a footer.</p>
  </footer>
`;
document.addEventListener('DOMContentLoaded', () => {
  console.log('footer.js loaded');
  const contentArea = document.getElementById('Footer-placeholder');
  if (!contentArea) {
    console.warn('Footer-placeholder not found in DOM');
    return;
  }
  contentArea.innerHTML = FooterHTML;
});

//Paste these into your html 
//<div id="Footer-placeholder"></div>
//<script src="footer.js"></script>
