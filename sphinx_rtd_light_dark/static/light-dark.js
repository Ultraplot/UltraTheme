/* Toggle light and dark theme
 * See: https://dev.to/ananyaneogi/create-a-dark-light-mode-switch-with-css-variables-34l8
 * CSS files from: https://github.com/richleland/pygments-css
 * Toggle functions and event handler
 * Best light themes: pastie, friendly, murhpy
 * Best dark themes: monokai, paraiso-dark
 */
var regex = /(.*)\/.*(\.css$)/i
const toggleSwitch = document.getElementById('light-dark-checkbox');
const pygmentsLink = document.getElementById('pygments-style');
const prefersDark = window.matchMedia('(prefers-color-scheme: dark)');
function lightToggle() {
    document.documentElement.setAttribute('data-theme', 'light');
    if (pygmentsLink) {
        pygmentsLink.href = pygmentsLink.href.replace(regex, '$1/pastie$2');
    }
    localStorage.setItem('theme', 'light');
}
function darkToggle() {
    document.documentElement.setAttribute('data-theme', 'dark');
    if (pygmentsLink) {
        pygmentsLink.href = pygmentsLink.href.replace(regex, '$1/monokai$2');
    }
    localStorage.setItem('theme', 'dark');
}
function switchTheme(e) {
    e.target.checked ? darkToggle() : lightToggle()
}
if (toggleSwitch) {
    toggleSwitch.addEventListener('change', switchTheme, null);
}

/* Check for user preference on load */
const currentTheme = localStorage.getItem('theme') || (prefersDark.matches ? 'dark' : 'light');
if (currentTheme === 'dark') {
    darkToggle();
    if (toggleSwitch) {
        toggleSwitch.checked = true;
    }
}
else {
    lightToggle();
    if (toggleSwitch) {
        toggleSwitch.checked = false;
    }
}
