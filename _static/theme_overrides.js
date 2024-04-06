const banner_text = `
NOTICE: You are viewing documentation for a development version of Security Onion.
<br>
View the <a href="https://docs.securityonion.net/">documentation for the latest stable release</a>.
`;

function show_banner() {
    if (READTHEDOCS_DATA['version'] == '2.4') return;

    const banner = document.createElement('div');
    banner.className = "so-banner";
    banner.innerHTML = banner_text;
    const rst = document.getElementsByClassName('rst-content')[0];
    console.log('rst=' + rst);
    rst.prepend(banner);
}

window.setTimeout(show_banner, 100);
