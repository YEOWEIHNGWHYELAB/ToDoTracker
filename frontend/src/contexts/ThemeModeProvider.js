import React, { useEffect, useState, useMemo } from 'react'
import PropTypes from "prop-types";
import { ThemeProvider, createTheme } from "@mui/material/styles";

export const ThemeModeContext = React.createContext({
    toggleThemeMode: () => { }
});

const getDesignTokens = (mode) => {
    return {
        palette: {
            mode
        }
    }
}

export default function ThemeModeProvider({ children }) {
    const [mode, setMode] = useState("dark"); // Defaults to dark Theme

    // Check the themeMode used in local storage, if can't get just set to dark
    useEffect(() => {
        const savedMode = localStorage.getItem('themeMode') || 'dark';
        setMode(savedMode);
    }, [setMode]);

    useEffect(() => {
        localStorage.setItem("themeMode", mode);
    }, [mode]);

    const themeMode = useMemo(() => {
        return {
            // Toggle Light/Dark Theme
            toggleThemeMode: () => {
                setMode((prevMode) => {
                    if (prevMode === "light") {
                        return "dark"
                    }
                    return "light"
                })
            }
        }
    }, [setMode]);

    const theme = useMemo(() => {
        return createTheme(getDesignTokens(mode))
    }, [mode])

    return (
        <ThemeModeContext.Provider value={themeMode}>
            <ThemeProvider theme={theme}>
                {children}
            </ThemeProvider>
        </ThemeModeContext.Provider>
    )
}

ThemeModeProvider.propTypes = {
    children: PropTypes.node
}