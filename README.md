# Hamster Kombat Api

## Examples
___
#### init client

```py
from scr import HamsterApiRequests

client = HamsterApiRequests()
```

#### Get daily reward

```py
await client.complete_daily_task()
```

#### Tap action

```py
import time

current_timestamp_seconds = time.time()
timestamp = int(current_timestamp_seconds * 1000)

await client.tap(
    taps_count=8000, # tap amount
    availableTaps=8000,
    timestamp=timestamp # milliseconds
)
```

#### Buy update ( card )

```py
await client.buy_update(upgradeId="oracle", timestamp=timestamp)
```

## Authorization bearer Token Instructions

### Step-by-Step Review and Correction

1. Get Chrome Extension -> https://chromewebstore.google.com/detail/resource-override/pkoacgokdfckfpndoffpifphamojphii

2. Create New rule

```js
if (location.hostname === "hamsterkombatgame.io") {
    const original_indexOf = Array.prototype.indexOf
    Array.prototype.indexOf = function (...args) {
        if (JSON.stringify(this) === JSON.stringify(['android', 'android_x', 'ios'])) {
            setTimeout(() => {
                Array.prototype.indexOf = original_indexOf
            })
            return 0
        }
        return original_indexOf.apply(this, args)
    }
}
```

3. Login into Telegram Web

4. Launch Hamster Kombat app

5. Open Developer Tools (F12), go to the Network tab, and find any requests to the hamster endpoint.

![end point example](https://habrastorage.org/webt/vq/vm/-j/vqvm-jwovxn_z8ltlwumyfm5a5g.png)

6. In the request headers, copy the Authorization bearer Token.

![Authorization token example](https://habrastorage.org/webt/s4/q8/sw/s4q8sw02fy_y1_wgbyn-osio-is.png)