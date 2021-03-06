// This is a minimal config.
// If you need the full config, get it from here:
// https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js

const colors = require('tailwindcss/colors')

module.exports = {
    purge: [
        // Templates within theme app (e.g. base.html)
        '../templates/**/*.html',
        // Templates in other apps. Uncomment the following line if it matches
        // your project structure or change it to match.
        // '../../templates/**/*.html',
    ],
    darkMode: false, // or 'media' or 'class'
    theme: {
        extend: {
            colors: {
                teal: colors.teal
            },
            fontFamily: {
                'montserrat': ['Montserrat Alternates']
            },
        },
    },
    variants: {
        extend: {},
    },
    plugins: [],
}
