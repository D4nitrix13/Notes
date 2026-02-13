// Author: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Email: danielperezdev@proton.me

/**
 * Generates a table header and appends it to the target table
 * @param {HTMLTableElement} table The target table element
 * @param {Array<string>} data An array of string names to be used as column headers
 * @returns {void}
 * @author D4nitrix13 <D4nitrix13.com>
 */
function generateTableHead(table, data) {
  const thead = table.createTHead();
  const row = thead.insertRow();
  for (const i of data) {
    const th = document.createElement("th");
    const text = document.createTextNode(i);

    th.appendChild(text);
    row.appendChild(th);
  }
}
