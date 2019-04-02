# Using browserify in a Django project

1. Create an empty `package.json` file.
  
   ```js
   {"private": true}
   ```

2. Run `npm install --save-dev browserify`.

3. Check to see if this works: `npx browserify <location_of_your_js_file>`

4. Replace sequential third-party JS script tags with `require`.

5. Run `npx browserify <location_of_your_js_file> -o <location_of_your_bundle>`

6. Update your Django templates to use the bundle file.

7. Check to make sure everything still works. If it does, you've solved the first problem! You'll have to run the above `browserify` command each time your change your JavaScript. Let's solve this.

8. Run `npm install --save-dev watchify`.

9. Now try `npx watchify <location_of_your_js_file> -o <location_of_your_bundle> -v`. This should write some output like 

   ```
   20963 bytes written to static/build/bundle.js (0.05 seconds) at 10:12:50
   ```

   You can now run this in a terminal to continuously watch for changes in your JavaScript and rebuild it.

10. Add the following to your `package.json`.

   ```js
    "scripts": {
      "watch": "watchify <source_js> --debug -v -o <bundle_js>",
      "build-dev": "browserify <source_js> --debug -o <bundle_js>",
      "build": "browserify <source_js> -o <bundle_js>"
    }
   ```

   You can now run `npm run build-dev` or `npm run watch` to run `browserify` and `watchify`.

11. Make sure you add `node_modules/` and your bundle file to `.gitignore`. I like to put my bundle in a directory like `static/build/` and ignore that directory.

12. To make this work with Heroku, run the following commands in your Heroku-enabled project:

    ```
    heroku buildpacks:set heroku/python
    heroku buildpacks:add --index 1 heroku/nodejs
    ```
