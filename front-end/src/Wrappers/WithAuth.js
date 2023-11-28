import { useContext, useEffect } from "react";
import { AuthContext } from "../Contexts/AuthContext";
import { useNavigate } from "react-router-dom";

export function withAuth(Component) {
    return (props) => {
        const { isAuthenticated } = useContext(AuthContext);
        const navigate = useNavigate();
        useEffect(() => {
            if (!isAuthenticated) {
                navigate("/login");
            }
        }, [isAuthenticated, navigate]);
        return <Component {...props}/>;
    };
}
