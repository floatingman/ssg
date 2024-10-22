# Static Site Generator

This project is a simple static site generator that converts Markdown files to HTML pages using a template.

## Features

- Converts Markdown files to HTML
- Uses a single HTML template for all pages
- Preserves directory structure from content to public
- Extracts titles from Markdown files
- Copies static files to the public directory

## Project Structure
```
project_root/
│
├── src/
│ ├── main.py
│ ├── build.py
│ └── markdown_blocks.py
│
├── content/
│ └── (Your Markdown files go here)
│
├── static/
│ └── (Your static files go here)
│
├── template.html
│
└── public/
└── (Generated HTML files will appear here)
```
## Setup

1. Ensure you have Python 3.6 or higher installed.
2. Clone this repository:
   ```
   git clone https://github.com/floatingman/ssg.git
   cd ssg
   ```
3. Create the necessary directories if they don't exist:
   ```
   mkdir -p content static public
   ```

## Usage

1. Place your Markdown files in the `content/` directory. You can use subdirectories to organize your content.
2. Put any static files (CSS, images, etc.) in the `static/` directory.
3. Edit the `template.html` file to customize the layout of your pages.
4. Run the static site generator:
   ```bash
   main.sh
   ```
5. The generated HTML files will be in the `public/` directory, maintaining the same structure as your `content/` directory.

## Tests
Unit tests can be ran with:

```bash
test.sh
```


## Customization

- Edit `template.html` to change the overall layout of your pages.
- Modify `src/markdown_blocks.py` to add support for additional Markdown features.
- Adjust `src/build.py` to change how files are processed or to add new functionality.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).