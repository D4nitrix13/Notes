// Type some code ->

const similar = "oO08 iIlL1 g9qCGQ"
const diacritics_etc = "â é ù ï ø ç Ã Ē Æ œ 🎵"

window.toggleFavorite = (alias) => {
    try {
        let favorites = JSON.parse(localStorage.getItem('favorites')) || []
        if (favorites.indexOf(alias) > -1) {
            favorites = favorites.filter((v) => {
                return v !== alias
            })
        } else {
            favorites.push(alias)
        }
        localStorage.setItem('favorites', JSON.stringify(Array.from(new Set(favorites))))
    } catch (err) {
        // eslint-disable-next-line no-console
        console.error('could not save favorite', err)
    }
    renderSelectList()
    return false
}