// lighthouserc.js
module.exports = {
    ci: {
      collect: {
        // Specify the directory where your site files (HTML, CSS, JS) are located
        staticDistDir: './build', // Adjust this path as necessary
      },
      assert: {
        // You can set up thresholds for scores, like performance scores
        preset: 'lighthouse:recommended',
        // For example, ensure performance score is >= 90
        "performance": 90
      },
      upload: {
        // Option 1: Upload reports to temporary public storage (easy)
        target: 'temporary-public-storage',
        // Option 2: Upload to a custom dashboard if set up
        // target: 'lhci-dashboard',
      },
    },
  };
  