import { useContext, useEffect } from "react";
import { AuthContext } from "../Contexts/AuthContext";
import { useNavigate } from "react-router-dom";

export function withUserAuth(Component) {
    return (props) => {
        const { isAuthenticated, entityType } = useContext(AuthContext);
        const navigate = useNavigate();
        useEffect(() => {
            if (!isAuthenticated) {
                navigate("/login");
            } else if (entityType === 'shelter') {
                navigate("/shelter-account");
            }
        }, [isAuthenticated, entityType, navigate]);
        return <Component {...props}/>;
    };
}
