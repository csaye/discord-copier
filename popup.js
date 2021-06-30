// get start button element
const startButton = document.getElementById("startButton");

// when start button clicked, inject copy function
startButton.addEventListener("click", async () => {
  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  // if current tab is discord
  if (tab.url.startsWith("https://discord.com")) {
    // execute start copy script
    chrome.scripting.executeScript({
      target: { tabId: tab.id },
      function: startCopy
    });
  // if tab not discord, throw alert
  } else alert("Extension must be run on Discord.");
});

// will be executed after copy starts
function startCopy() {}
