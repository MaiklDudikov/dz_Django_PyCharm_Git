// Замените YOUR_API_KEY вашим API ключом от OMDB API b17a476
const API_KEY = 'b17a476';
const BASE_URL = 'https://www.omdbapi.com/';

// DOM элементы
const searchForm = document.getElementById('search-form');
const moviesList = document.getElementById('movies-list');
const pagination = document.getElementById('pagination');
const detailsContainer = document.getElementById('details-container');
const movieDetailsSection = document.getElementById('movie-details');

let currentPage = 1;
let totalResults = 0;
let searchQuery = '';
let searchType = 'movie';

// Функция поиска фильмов
searchForm.addEventListener('submit', (e) => {
    e.preventDefault();
    searchQuery = document.getElementById('title').value;
    searchType = document.getElementById('type').value;
    currentPage = 1;
    searchMovies();
});

// Отправляем запрос на OMDB API для поиска фильмов
async function searchMovies() {
    const url = `${BASE_URL}?s=${searchQuery}&type=${searchType}&page=${currentPage}&apikey=${API_KEY}`;
    const response = await fetch(url);
    const data = await response.json();

    if (data.Response === 'True') {
        totalResults = parseInt(data.totalResults);
        displayMovies(data.Search);
        setupPagination();
    } else {
        moviesList.innerHTML = '<p>Movie not found!</p>';
        pagination.innerHTML = '';
        movieDetailsSection.classList.add('hidden');
    }
}

// Отображаем список фильмов
function displayMovies(movies) {
    moviesList.innerHTML = '';
    movies.forEach(movie => {
        const movieCard = document.createElement('div');
        movieCard.classList.add('movie-card');
        movieCard.innerHTML = `
            <img src="${movie.Poster !== 'N/A' ? movie.Poster : 'no-poster.png'}" alt="Poster">
            <h4>${movie.Title}</h4>
            <p>${movie.Year}</p>
            <button onclick="getMovieDetails('${movie.imdbID}')">Details</button>
        `;
        moviesList.appendChild(movieCard);
    });
}

// Настройка пагинации
function setupPagination() {
    pagination.innerHTML = '';
    const totalPages = Math.ceil(totalResults / 10);

    for (let i = 1; i <= totalPages; i++) {
        const button = document.createElement('button');
        button.textContent = i;
        button.disabled = (i === currentPage);
        button.addEventListener('click', () => {
            currentPage = i;
            searchMovies();
        });
        pagination.appendChild(button);
    }
}

// Получение информации о фильме по ID
async function getMovieDetails(imdbID) {
    const url = `${BASE_URL}?i=${imdbID}&apikey=${API_KEY}`;
    const response = await fetch(url);
    const data = await response.json();

    if (data.Response === 'True') {
        displayMovieDetails(data);
    }
}

// Отображение подробной информации о фильме
function displayMovieDetails(movie) {
    detailsContainer.innerHTML = `
        <div class="movie-details">
            <img src="${movie.Poster !== 'N/A' ? movie.Poster : 'no-poster.png'}" alt="Poster">
            <div>
                <p><strong>Title:</strong> ${movie.Title}</p>
                <p><strong>Released:</strong> ${movie.Released}</p>
                <p><strong>Genre:</strong> ${movie.Genre}</p>
                <p><strong>Country:</strong> ${movie.Country}</p>
                <p><strong>Director:</strong> ${movie.Director}</p>
                <p><strong>Writer:</strong> ${movie.Writer}</p>
                <p><strong>Actors:</strong> ${movie.Actors}</p>
                <p><strong>Awards:</strong> ${movie.Awards}</p>
            </div>
        </div>
    `;
    movieDetailsSection.classList.remove('hidden');
}
