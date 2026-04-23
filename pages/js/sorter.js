/**
 * Toggles the text and data attribute of the direction buttons
 */
function toggleDir(btn) {
    const isAsc = btn.dataset.dir === "asc";
    btn.dataset.dir = isAsc ? "desc" : "asc";
    
    // Update label based on context
    const field = btn.id === "primary-dir" ? 
                  document.getElementById('primary-sort').value : 
                  document.getElementById('secondary-sort').value;
    
    const isNumeric = !['name', 'tier'].includes(field);
    
    if (isNumeric) {
        btn.innerText = btn.dataset.dir === "asc" ? "Low ↑" : "High ↓";
    } else {
        btn.innerText = btn.dataset.dir === "asc" ? "A-Z" : "Z-A";
    }
}

/**
 * Main function triggered by the "Apply" button
 */
function applyDexChanges() {
    const container = document.getElementById("dex-grid");
    const cards = Array.from(container.getElementsByClassName("dex-card"));
    
    const searchVal = document.getElementById("dex-search").value.toLowerCase();
    
    const pField = document.getElementById("primary-sort").value;
    const pDir = document.getElementById("primary-dir").dataset.dir;
    
    const sField = document.getElementById("secondary-sort").value;
    const sDir = document.getElementById("secondary-dir").dataset.dir;

    const tierOrder = { "Uber": 1, "OU": 2, "UU": 3, "RU": 4, "NU": 5, "PU": 6, "LC": 7, "Untiered": 8 };

    function getVal(el, field) {
        let val = el.dataset[field];
        if (!['name', 'tier'].includes(field)) return parseInt(val, 10) || 0;
        if (field === 'tier') return tierOrder[val] || 99;
        return val; // string name
    }

    cards.sort((a, b) => {
        // 1. Primary Sort
        let vA = getVal(a, pField);
        let vB = getVal(b, pField);
        
        if (vA !== vB) {
            if (vA < vB) return pDir === "asc" ? -1 : 1;
            if (vA > vB) return pDir === "asc" ? 1 : -1;
        }

        // 2. Secondary Sort (if not "none")
        if (sField !== "none") {
            vA = getVal(a, sField);
            vB = getVal(b, sField);
            if (vA !== vB) {
                if (vA < vB) return sDir === "asc" ? -1 : 1;
                if (vA > vB) return sDir === "asc" ? 1 : -1;
            }
        }

        // 3. Final Fallback (Always Name A-Z)
        return a.dataset.name.localeCompare(b.dataset.name);
    });

    // Apply visibility and order
    cards.forEach(card => {
        const matches = card.dataset.name.toLowerCase().includes(searchVal);
        card.style.display = matches ? "" : "none";
        container.appendChild(card);
    });
}