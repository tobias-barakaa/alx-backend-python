<!-- async_python.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Asynchronous Programming in Python</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            line-height: 1.6;
        }
        code {
            background-color: #f4f4f4;
            padding: 2px 4px;
            border: 1px solid #ddd;
            font-size: 90%;
            color: #333;
            border-radius: 4px;
        }
    </style>
</head>
<body>

<h1>Asynchronous Programming in Python</h1>

<p>Asynchronous programming in Python allows you to write non-blocking code, particularly useful for I/O-bound tasks, by using the <code>async</code> and <code>await</code> keywords.</p>

<h2>Async Functions</h2>

<p>Async functions are defined using the <code>async def</code> syntax. They can contain <code>await</code> expressions to pause the execution of the function while waiting for asynchronous operations to complete.</p>

<pre><code>
async def my_async_function():
    print("Start")
    await asyncio.sleep(1)
    print("End")
</code></pre>

<h2>Running Concurrent Coroutines</h2>

<p>You can run concurrent coroutines using the <code>asyncio.gather</code> function or create tasks with <code>asyncio.create_task</code>.</p>

<pre><code>
import asyncio

async def coroutine1():
    print("Coroutine 1 start")
    await asyncio.sleep(2)
    print("Coroutine 1 end")

async def coroutine2():
    print("Coroutine 2 start")
    await asyncio.sleep(1)
    print("Coroutine 2 end")

async def main():
    # Run coroutines concurrently using asyncio.gather
    await asyncio.gather(coroutine1(), coroutine2())

    # OR create tasks with asyncio.create_task
    # task1 = asyncio.create_task(coroutine1())
    # task2 = asyncio.create_task(coroutine2())
    # await asyncio.gather(task1, task2)
</code></pre>

<p>Remember to run your code within the event loop using <code>asyncio.run(main())</code> or within an existing event loop.</p>

<h2>References</h2>

<ul>
    <li><a href="https://docs.python.org/3/library/asyncio.html" target="_blank">Python asyncio Documentation</a></li>
</ul>

</body>
</html>
