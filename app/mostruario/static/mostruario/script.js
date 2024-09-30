
let back_to_top_button = document.getElementById("btn-back-to-top");

window.onscroll = function () {
  scrollFunction();
};

function scrollFunction() {
  if (
    document.body.scrollTop > 20 ||
    document.documentElement.scrollTop > 20
  ) {
    back_to_top_button.style.display = "block";
  } else {
    back_to_top_button.style.display = "none";
  }
}

back_to_top_button.addEventListener("click", backToTop);

function backToTop() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}

document.getElementById('add-item-btn').addEventListener('click', function () {
  document.getElementById('add-item-form').classList.remove('d-none'); // Mostra o formulário
  document.getElementById('add-item-btn').classList.add('d-none'); // Esconde o botão +
});


function cancelAddItem() {
  document.getElementById('add-item-form').classList.add('d-none'); // Esconde o formulário
  document.getElementById('add-item-btn').classList.remove('d-none'); // Mostra o botão +
}

function toggleEditForm(itemId) {
  console.log(itemId);

  var itemElement = document.querySelector('[data-id="' + itemId + '"]');

  if (itemElement) {
    var buttonGroup = itemElement.querySelector('.button-group');
    var editForm = itemElement.querySelector('.edit-form');

    if (editForm.classList.contains('d-none')) {
      editForm.classList.remove('d-none');
      buttonGroup.classList.add('d-none');
    } else {
      editForm.classList.add('d-none');
      buttonGroup.classList.remove('d-none');
    }
  }
}

function filterItems(category) {
  console.log('Filtrando por categoria:', category);

  let items = document.querySelectorAll('.item'); 
  let buttons = document.querySelectorAll('.filter-button'); 

  items.forEach(function (item) {
    let itemCategory = item.getAttribute('data-category'); 

    if (category === 'all' || itemCategory === category) {
      item.style.display = 'block'; 
      item.style.display = 'none'; 
    }
  });

  buttons.forEach(function (button) {
    button.classList.remove('active-filter');
  });

  document.querySelector(`button[onclick="filterItems('${category}')"]`).classList.add('active-filter');
}

function handleFilterChange() {
const category = new URLSearchParams(window.location.search).get('category') || 'all';

const sort = document.getElementById('sort').value;

const url = `?category=${category}&sort=${sort}`;

window.location.href = url;
}