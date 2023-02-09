for (let i = 1; i <= 100; i++) {
  $(`#scale-${i}`).click(function() {
    $(`#scale-${i}`).addClass('button-clicked');
});
  $(`a${i}`).hide();
  $(`#scale2-${i}`).click(function() {
    $(`a${i}`).show();
    $(`#scale2-${i}`).append( $( `a${i}` ) );
});
}

