function expandSearch() {
    var searchInput = document.querySelector('.search-click');
    searchInput.classList.toggle('expanded');
    if (searchInput.classList.contains('expanded')) {
        searchInput.focus();
    } else {
        searchInput.blur();
    }
}
