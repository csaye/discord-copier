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
function startCopy() {
  // will be called when messages change
  function onMutation(mutations) {
    for (const mutation of mutations) {
      for (const addedNode of mutation.addedNodes) {
        console.log(addedNode.textContent);
      }
    }
  }

  // get messages scroller and set up mutation observer
  const scrollerInner = document.querySelector("div[data-list-id='chat-messages']");
  new MutationObserver(onMutation).observe(scrollerInner, { childList: true });
  alert('Mutation observer started.');
}
