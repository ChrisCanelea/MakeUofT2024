## Inspiration
Mornings can be rough at times, with you rushing to get out the door on time, even skipping breakfast if needed, only to get to your bus stop and end up waiting half an hour anyways due to delays. This frustrating situation is our motivation for the creation of the Intelligent Residence system, a smart home appliance that aims to save as much of your time as possible.

## What it does
Utilizing a Raspberry Pi for the main terminal, its primary feature is to be configured with a transit route (TTC  buses for now), and query live arrival times for that route, displaying them for your convenience. From just a glance, you can see when the next few buses arrive, allowing you to plan your departure to maximize your time in comfort at home. This avoids unnecessary waiting at the station so that you can finish that breakfast you usually would have skipped.

## How we built it
We started by creating basic server/client interactions with ESP8266 boards to get us familiar with the environment. In parallel, we also worked on fetching and parsing TTC data, and developed a UI for the R-PI terminal. Once the individual parts were working, we integrated the systems and allowed them to interact with each other using our own protocol/method for communication. A lot of time was spent debugging and fine-tuning our system into a rather polished and scalable prototype.

## Challenges we ran into
This marks our group's initial endeavour to interface with a public API. We opted for the UmoIQ API, which offers real-time feedback on public transportation vehicles and delivers arrival predictions through XML files. The journey presented its fair share of challenges, primarily stemming from API documentation that proved less than clear. Given the time constraints, these challenges added significant pressure to our efforts.

Furthermore, in the implementation phase, we decided to adopt an asynchronous approach for the server, which processes communications from wireless devices. However, as the design implementation advanced, our group transitioned to a conversation-like approach for all server-client communication. This shift has introduced challenging bugs to resolve because the server processes tasks asynchronously while all communication occurs synchronously.

## Accomplishments that we're proud of
The group takes great pride in presenting a design that not only encompasses all the intended functionalities but also surpasses our expectations. We feel like the UI is clean and intuitive, the connections are handled intelligently, and overall we are proud to have created a system utilizing technology we were unfamiliar with.

## What we learned
The design journey has fostered personal growth among every team member. Whether it involved mastering UI design and server communication in a new language like Python, constructing a server that facilitates WIFI communication for wireless interactions, or delving into Extract, Transform, and Load (ETL) processes from a public API, each team member has experienced significant learning and development. 

## What's next for Intelligent Residence
Our first order of business would be to add live arrival times of other transit modes such as the TTC subway and the GO train. Furthermore, since the server is already set up asynchronously, it lets us add new clients and send requests whenever we want. This means our design is scalable with all kinds of other appliances, a few of which we already planned and either implemented partially or failed to implement in time. The placeholders "App 2" and "App 3" were in preparation for these other appliances. These were ideas such as:
- The power saver / appliance toggle: Turns off appliances that are left on from the press of a button
- The shopping list: An interface in the kitchen to add items to a shopping list in the moment with ease
- The outlet tracker: A device to track the battery levels of devices plugged into the wall, unplugging them close to full charge and reporting when you forgot to charge a device
- The alarm watch: A vibrating add on to your watch with a configurable timer

**All the information for our appliances would be managed by the server/local access point, unifying all these capabilities into one smart home system: The Intelligent Residence.**