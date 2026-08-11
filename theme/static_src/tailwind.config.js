/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        '../../templates/**/*.html',
        '../../reviews/templates/**/*.html',
        './src/**/*.{js,css}',
    ],
    theme: {
        extend: {
            colors: {
                /* NVIDIA Green brand scale */
                primary: {
                    DEFAULT: '#76b900',
                    50: '#f6fce8',
                    100: '#eaf9c9',
                    200: '#d8f29b',
                    300: '#c3e968',
                    400: '#9fd63a',
                    500: '#76b900',   /* NVIDIA Green */
                    600: '#5a8d00',   /* NVIDIA Green Dark */
                    700: '#476f00',
                    800: '#3a5c00',
                    900: '#2d4800',
                },
                /* Design system tokens */
                canvas: '#ffffff',
                soft: '#f7f7f7',
                ink: '#000000',
                body: '#1a1a1a',
                mute: '#757575',
                stone: '#898989',
                ash: '#a7a7a7',
                elevated: '#1a1a1a',
                hairline: '#cccccc',
                'hairline-strong': '#5e5e5e',
                'accent-pale': '#bff230',
                'link-blue': '#0046a4',
                success: '#3f8500',
                'error-deep': '#650b0b',
                error: '#e52020',
                warning: '#df6500',
                'warning-bright': '#ef9100',
            },
            fontFamily: {
                sans: ['Inter', 'Arial', 'Helvetica', 'sans-serif'],
                display: ['Inter', 'Arial', 'Helvetica', 'sans-serif'],
            },
            borderRadius: {
                none: '0px',
                xs: '1px',
                sm: '2px',
                DEFAULT: '2px',
                md: '2px',
                lg: '2px',
                full: '9999px',
            },
            boxShadow: {
                chrome: '0 0 5px 0 rgba(0,0,0,0.3)',
            },
            maxWidth: {
                content: '1280px',
            },
        },
    },
    plugins: [
        require('@tailwindcss/typography'),
        require('@tailwindcss/forms'),
    ],
}
