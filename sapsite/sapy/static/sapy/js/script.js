for (let i = 1; i <= 100; i++) {
  $(`#scale-${i}`).click(function() {
    $(`#scale-${i}`).addClass('button-clicked');
});
  $(`#scale2-${i}`).click(function() {
    $(`#scale2-${i}`).append( $( `strong${i}` ) );
});
}

