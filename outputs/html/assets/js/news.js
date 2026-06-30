document.addEventListener("DOMContentLoaded", function () {
  // Home page search + category filtering
  const homeSearchInput = document.querySelector("#home-search-input");
  const newsCards = document.querySelectorAll(".news-card");
  const categoryButtons = document.querySelectorAll(".category-filter-btn");

  let selectedCategory = "all";

  function filterNews() {
    const query = (homeSearchInput && homeSearchInput.value || "").toLowerCase();

    newsCards.forEach(function (card) {
      const text = card.dataset.search || "";
      const category = card.dataset.category || "genel";

      const matchesSearch = text.includes(query);
      const matchesCategory = selectedCategory === "all" || category === selectedCategory;

      if (matchesSearch && matchesCategory) {
        card.style.display = "block";
      } else {
        card.style.display = "none";
      }
    });
  }

  if (homeSearchInput) {
    homeSearchInput.addEventListener("input", filterNews);
  }

  if (categoryButtons && categoryButtons.length) {
    categoryButtons.forEach(function (button) {
      button.addEventListener("click", function () {
        categoryButtons.forEach(function (btn) {
          btn.classList.remove("active");
        });

        button.classList.add("active");
        selectedCategory = button.dataset.category;

        filterNews();
      });
    });
  }

  // Search page: fetch index and display
  const searchInput = document.querySelector("#search-input");
  const resultsContainer = document.querySelector("#search-results");

  if (searchInput && resultsContainer) {
    let newsData = [];

    fetch("data/index/search-index.json")
      .then(response => response.json())
      .then(data => {
        newsData = data;
        showResults(newsData);
      })
      .catch(() => { resultsContainer.innerHTML = "<p style='color:var(--muted)'>Arama indeksi yüklenemedi.</p>"; });

    function showResults(items) {
      resultsContainer.innerHTML = "";

      items.forEach(item => {
        const card = document.createElement("div");
        card.className = "news-card";

        card.innerHTML = `
          <h2>${item.title || ""}</h2>
          <p>${item.summary || ""}</p>
          <p>
            <strong>Kategori:</strong> ${item.category || "genel"}
            |
            <strong>Kaynak:</strong> ${item.source || ""}
          </p>
          <a href="${item.link}" target="_blank">Haberi Oku</a>
          <hr>
        `;

        resultsContainer.appendChild(card);
      });
    }

    searchInput.addEventListener("input", () => {
      const query = (searchInput.value || "").toLowerCase();

      const filteredNews = newsData.filter(item => {
        const text = `
          ${item.title || ""}
          ${item.summary || ""}
          ${item.category || ""}
          ${item.source || ""}
          ${item.published || ""}
        `.toLowerCase();

        return text.includes(query);
      });

      showResults(filteredNews);
    });
  }
});
