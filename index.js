const fileNames = ['game_data.json', 'game_urls.json', 'game_frequency.json'];

const fetchJson = async (fileName) => {
  const response = await fetch(fileName);
  if (!response.ok) {
    throw new Error(`Failed to fetch ${fileName}`);
  }
  return response.json();
};

const capitalizeFirstLetter = (str) => {
  return str.replace(/\b\w/g, match => match.toUpperCase());
};

Promise.all(fileNames.map(fetchJson))
  .then(dataArray => {
    const gameData = dataArray[0];
    const urlData = dataArray[1];
    const frequencyData = dataArray[2];

    // Sort the games by frequency in descending order
    const sortedGames = Object.entries(frequencyData)
      .sort((a, b) => b[1] - a[1])
      .map(([game, frequency]) => ({
        game: capitalizeFirstLetter(game),
        releaseDate: gameData[game] ? gameData[game].release_date : "N/A",
        mention: frequency,
        redditPosts: urlData[game] || []
      }));

    // Create and append a table to the HTML document
    const tableContainer = document.getElementById('gameTableContainer');
    const table = document.createElement('table');
    table.innerHTML = `
      <thead>
        <tr>
          <th>Game</th>
          <th>Release Date</th>
          <th>Mentions</th>
          <th>Reddit Posts</th>
        </tr>
      </thead>
      <tbody>
        ${sortedGames.map(({ game, releaseDate, mention, redditPosts }) => `
          <tr>
            <td>${game}</td>
            <td>${releaseDate}</td>
            <td>${mention}</td>
            <td>${redditPosts.map((postId, index) => `
              <a href="https://www.reddit.com/${postId}" target="_blank">Reddit Post ${index + 1}</a>
            `).join(', ')}</td>
          </tr>
          <tr><td colspan="4"><hr></td></tr>
        `).join('')}
      </tbody>
    `;
    tableContainer.appendChild(table);
  })
  .catch(error => console.error('Error fetching or parsing JSON:', error));

  function updateCountdown() {
    const now = new Date();
    const nextUpdate = new Date(now);
    nextUpdate.setHours(20, 0, 0, 0); // Set the next update time to 8:00 PM
  
    let timeDiff = nextUpdate - now;
  
    if (timeDiff < 0) {
      // If the next update time has already passed for today, set it for tomorrow
      nextUpdate.setDate(now.getDate() + 1);
      timeDiff = nextUpdate - now;
    }
  
    if (timeDiff === 0) {
      document.getElementById('countdown').innerHTML = 'Next Update: Happening now!';
    } else {
      const hours = Math.floor(timeDiff / (1000 * 60 * 60));
      const minutes = Math.floor((timeDiff % (1000 * 60 * 60)) / (1000 * 60));
      const seconds = Math.floor((timeDiff % (1000 * 60)) / 1000);
  
      document.getElementById('countdown').innerHTML = `Next Update: ${hours}h ${minutes}m ${seconds}s`;
    }
  
    // Update the countdown every second
    setTimeout(updateCountdown, 1000);
  }
  
  // Initial call to start the countdown
  updateCountdown();
  