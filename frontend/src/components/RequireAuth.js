import React from 'react';
import { Navigate, Outlet } from "react-router-dom";

import { AuthContext } from 'src/contexts/AuthContextProvider';

export default function RequireAuth() {

    const { isAuthenticated } = React.useContext(AuthContext);

    if (isAuthenticated === null) {
        return <div>Loading...</div>
    }

    // Return based on the routing route if isAutenticated
    if (isAuthenticated === true) {
        return <Outlet />
    }


    return (
        <Navigate to="/auth/signin" />
    )
}
