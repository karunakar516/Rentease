
const searchInput = document.getElementById('search');
const cards = document.getElementsByClassName('card');
searchInput.addEventListener('keyup', function() {
  const searchTerm = searchInput.value.toLowerCase();

  for (let i = 0; i < cards.length; i++) {
    const cardTitle = cards[i].querySelector('.card-title').textContent.toLowerCase();
    const cardContent = cards[i].querySelector('.card-body p').textContent.toLowerCase();
    if (cardContent.includes(searchTerm)|| cardTitle.includes(searchTerm)) {
      cards[i].style.display = 'block';
    } 
    else {
      cards[i].style.display = 'none';
    }
  }
});
