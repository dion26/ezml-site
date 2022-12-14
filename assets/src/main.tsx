import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import App from './App';
import { CssBaseline } from '@mui/material';
import store from './store'
import { Provider } from 'react-redux'

import ThemeModeProvider from './theme/context/ThemeModeContext';
import ThemeSchemeProvider from './theme/context/ThemeSchemeContext';
import M3ThemeProvider from './theme/m3/M3ThemeProvider';

const root = createRoot(document.getElementById('root')!);

root.render(
    <ThemeModeProvider>
        <ThemeSchemeProvider>
            <M3ThemeProvider>
                <CssBaseline enableColorScheme />
                {/* <Provider store={store}> */}
                    <App />
                {/* </Provider> */}
            </M3ThemeProvider>
        </ThemeSchemeProvider>
    </ThemeModeProvider>
);
