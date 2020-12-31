$(() => {
    $('body').on('change', 'input[data-line-item]', () => {
        generateNewBasketTable();
        generateNewTimeEstimate();
    }); 
    generateNewBasketTable();
    generateNewTimeEstimate();

    $('#checkout-button').on('click', () => {
        $('form').submit();
    })

});

function prettifyOutput(input) {
    let output = "";
    input = input.split("_");
    for(let word of input) {
        output += `${word[0].toUpperCase()}${word.substring(1)} `;
    }
    return output;
}

function generateNewBasketTable() {
    $('.basket tbody').html("");
    let lineItems = $("input[data-line-item]:checked");
    const deposit = 30;
    
    let totalCost = deposit;

    addLineToTable("Deposit", "Non-Refundable", deposit);

    $.each(lineItems, (idx, item) => {
        let lineItemName = prettifyOutput($(item).data("line-item"));
        let itemName = prettifyOutput($(item).val());
        let additionalCost = parseInt($(item).data('additional-cost'));

        totalCost += additionalCost;
        
        addLineToTable(lineItemName, itemName, additionalCost);
    });
    addSubtotalToTable("SubTotal", totalCost);
    if (checkRequiredFields()) {
        $('#checkout-button').attr('disabled', false);
    } else {
        $('#checkout-button').attr('disabled', true);
    }
}

function generateNewTimeEstimate() {

    let lineItems = $("input[data-line-item]:checked");
    const baseTime = 7;
    let totalTime = baseTime;

    $.each(lineItems, (idx, item) => {
        let additionalTime = parseFloat($(item).data('additional-time-multiplier'));
        totalTime *= additionalTime;
    });

    $('.estimated-time').html(Math.ceil(totalTime));
}


function addLineToTable(lineItemName, itemName, cost) {
    $('.basket tbody').append(`<tr><td>${lineItemName}</td><td>${itemName}</td><td>£${cost.toFixed(2)}</td></tr>`);
}

function addSubtotalToTable(title, cost) {
    $('.basket tbody').append(`<tr><th colspan="2">${title}</th><td>£${cost.toFixed(2)}</td></tr>`);
}

function checkRequiredFields() {
    console.log($(`input[data-line-item="draw_type"]:checked`))
    let drawTypeChosen = $(`input[data-line-item="draw_type"]:checked`).length == 1;
    let colourChosen = $(`input[data-line-item="colour"]:checked`).length == 1;
    let backingChosen = $(`input[data-line-item="backing"]:checked`).length == 1;
    let filesChosen = $(`input[data-line-item="files"]:checked`).length == 1;
    return drawTypeChosen && colourChosen && backingChosen && filesChosen;
}