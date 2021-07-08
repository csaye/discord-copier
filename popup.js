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
  let lastText = undefined;

  // will be called when messages change
  function onMutation(mutations) {
    for (const mutation of mutations) {
      for (const addedNode of mutation.addedNodes) {
        // skip if doubled message
        if (addedNode.textContent === lastText) continue;
        else lastText = addedNode.textContent;
        // get styled message content
        const content = addedNode.children[0].children;
        if (!content.length) continue;
        const message = content.length === 2 ?
        `**${content[0]?.textContent?.trim()}** ${content[1]?.textContent}` :
        `**${content[1]?.textContent?.trim()}** ${content[2]?.textContent}`;
        console.log(message);
        // create new connection and send content
        const connection = new WebSocket("ws://localhost:9999");
        connection.onopen = e => connection.send(message);
        connection.onerror = e => alert('WebSocket connection failed. Make sure you have started the server.');
      }
    }
  }

  // get messages scroller and set up mutation observer
  const scrollerInner = document.querySelector("div[data-list-id='chat-messages']");
  new MutationObserver(onMutation).observe(scrollerInner, { childList: true });
  alert('Mutation observer started.');
}
