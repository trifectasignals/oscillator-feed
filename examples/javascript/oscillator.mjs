// Read the Trifecta Oscillator feed and print the current reading.
//
// The Trifecta Oscillator is a market-breadth oscillator published by
// Trifecta Signals after each U.S. market close. The feed is free to
// read and display with attribution — see the repository README for
// terms.
//
// Feed: https://trifectasignals.com/oscillator.json
// Page: https://trifectasignals.com/oscillator
//
// Run with Node 18+:  node oscillator.mjs

const FEED_URL = "https://trifectasignals.com/oscillator.json";

const res = await fetch(FEED_URL);
if (!res.ok) throw new Error(`Feed request failed: ${res.status}`);
const feed = await res.json();

console.log(`${feed.gauge} — as of ${feed.asOf} (${feed.basis})`);
console.log(`Value: ${feed.value.toFixed(2)}  Zone: ${feed.zone}`);
console.log(
  `Previous close (${feed.prevDate}): ${feed.prevValue.toFixed(2)} ` +
    `(${feed.prevZone})  Change: ${feed.change >= 0 ? "+" : ""}${feed.change.toFixed(2)}`
);
if (feed.episodeDay) {
  console.log(
    `Oversold episode: day ${feed.episodeDay} (began ${feed.firstOversold})`
  );
}
