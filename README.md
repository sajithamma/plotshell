
# Plot: AI Helper for DevOps

🚀 Plot is a powerful command-line tool designed to provide immediate assistance to DevOps professionals. It leverages the capabilities of OpenAI's GPT models to deliver precise command guidance tailored to various operating systems and environments.

## Features 🌟

- **Streamlined Command Assistance**: Get specific commands for your operating system without unnecessary clutter.
- **Support for Multiple GPT Models**: Choose between different GPT models like GPT-4 for tailored assistance.
- **Easy Configuration**: Simple commands to set your API key and preferred GPT model.

## Installation 🛠️

To install Plot, simply use pip. Ensure you have Python 3.6 or later installed.

```bash
pip install plotshell
```

## Configuration 🔧

Before you start using Plot, you need to configure your OpenAI API key. Optionally, you can also set your preferred GPT model if you don't want to use the default (GPT-4).

### Setting the API Key

```bash
plot --setkey
```

When prompted, enter your OpenAI API key. This key will be saved and used for future requests.

### Setting the GPT Model

If you want to use a different model than the default GPT-4, you can set it as follows:

```bash
plot --set-model gpt-3.5-turbo
```

This command will save your model choice and use it for all future inquiries.

## Usage 📝

To use Plot, simply type `plot` followed by the command or query you need help with. Here’s how it works:

```bash
plot how to setup nginx
```

### Examples

Here are a few examples of how you can use Plot to get help with common DevOps tasks:

- **Setting up nginx**:
```bash
plot setup nginx webserver
```

- **Initializing a Git repository**:
```bash
plot how to initialize git repository
```

- **Creating a Python virtual environment**:
```bash
plot create python virtual environment
```
