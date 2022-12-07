# bloXroute-newTxs-test
# QA Home Assignment

This home assignment consists ot two parts:
1. create a regression test plan for the newTxs stream (foucsing on the `includes` and `filters` option)
2. implement some of the tests in the regression test plan from step 1 using Python

## part 1 - regression test plan
newTxs stream is one services that we provide to our customers. Customer bot (same as your python program) opens a [websocket] connection and subscribe to one of our [streams].
The test cases should be for regression tests, checking if something that works before continue to work with a new version (you can assume that what current version is stable and it can be used as the baseline). Focus on testing the [newTxs] stream and within it on the `include` and [filters] options.

## part 2 - implementing the regression tests
You can use Python (you can use python 3.9 and above)
Examples on Python code that works can be found in our documentation website:
* [creating a subscription]
* [handling notifications]

## subscribe to bloXroute services
In order to use our services you need an account, please [register] to our services (it's free, no credit card is required).
Once registered, you need to send me your account-id / email and we will upgrade your tier to Professional so you can use all the fields in the include.

I will check the following:
* asking about the tests cases in the regression tests cases (I know there can be many and you did not cover all)
* Readable and maintainable code
* Level of knowledge in the submitted code
* Checking code can run
 
You have one calendar week to submit the regression test plan and the code
Good luck

[websocket]: https://en.wikipedia.org/wiki/WebSocket
[streams]: https://docs.bloxroute.com/streams/working-with-streams
[newTxs]: https://docs.bloxroute.com/streams/newtxs-and-pendingtxs
[filters]: https://docs.bloxroute.com/streams/newtxs-and-pendingtxs/filter
[creating a subscription]: https://docs.bloxroute.com/streams/working-with-streams/creating-a-subscription
[handling notifications]: https://docs.bloxroute.com/streams/working-with-streams/handling-the-notification
[register]: https://portal.bloxroute.com
