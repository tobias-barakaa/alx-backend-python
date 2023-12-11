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

```python
<pre><code>
async def my_async_function():
    print("Start")
    await asyncio.sleep(1)
    print("End")
</code></pre>

