// script.js

$(function() {
    // Function to handle showing modal with asset details
    function showModal(data) {
        let modalBody = $('#modalBody');
        modalBody.empty();
        Object.entries(data).forEach(([key, value]) => {
            let row = `<tr><th>${key}</th><td>${value}</td></tr>`;
            modalBody.append(row);
        });
        $('#assetModal').modal('show');
    }

    // Function to filter table based on asset code
    function filterTable(query, allData) {
        const filteredData = allData.find(row => {
            const assetCode = row['Asset Code'];
            return assetCode && assetCode.toLowerCase() === query.toLowerCase();
        });

        if (filteredData) {
            showModal(filteredData);
        } else {
            console.log(`Asset with code '${query}' not found.`);
            // Handle case where no matching asset code is found
            // Optionally, you could display a message or handle the case differently.
        }
    }

    // Click event for search button
    $('#searchButton').on('click', function() {
        const query = $('#search').val().trim();
        filterTable(query, allData);
    });

    // Autocomplete initialization and keypress event
    fetch('/data')
        .then(response => response.json())
        .then(data => {
            allData = data;

            // Initialize autocomplete on #search input field
            $('#search').autocomplete({
                source: data.map(row => row['Asset Code']),
                select: function(event, ui) {
                    filterTable(ui.item.value, allData);
                }
            });

            // Keypress event for Enter key in search input
            $('#search').on('keypress', function(e) {
                if (e.which === 13) { // Enter key pressed
                    const query = $(this).val().trim();
                    filterTable(query, allData);
                }
            });
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
});
