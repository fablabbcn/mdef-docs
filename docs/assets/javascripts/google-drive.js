"use strict";
class GDriveFolderEmbed extends HTMLElement {
  constructor() {
    super();
    const shadowRoot = this.attachShadow({ mode: "open" });
  }
  static get observedAttributes() {
    return ["folderID", "render"];
  }
  async connectedCallback() {
    const folder = `${this.getAttribute("folderID")}`;
    const show = `${this.getAttribute("render")}`;
    const url =
      "https://drive.google.com/embeddedfolderview?id=" + folder + "#" + show;
    const button_url = 
      "https://drive.google.com/drive/folders/" + folder;
    this.shadowRoot.innerHTML = `
    <iframe style="
    width:100%;
    height: 40vh;
    z-index: 9999;
    border: none" 
  src=${url} webkitallowfullscreen="" mozallowfullscreen="" sandbox="allow-forms allow-scripts allow-popups allow-same-origin allow-pointer-lock" allowfullscreen="" frameBorder="0" scrolling="auto" loading="lazy" seamless></iframe>
  <a target="_blank" class="md-button md-button--primary" href="${button_url}">Open Drive folder</a>
  `;
  }
}
// optional
const deepFreeze = (obj) => {
  Object.keys(obj).forEach((prop) => {
    if (typeof obj[prop] === "object") deepFreeze(obj[prop]);
  });
  return Object.seal(obj);
};
const frozenComponent = deepFreeze(GDriveFolderEmbed);
customElements.define("gdf-embed", frozenComponent);