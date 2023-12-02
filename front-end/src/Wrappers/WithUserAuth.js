import { useContext, useEffect } from "react";
import { AuthContext } from "../Contexts/AuthContext";
import { useNavigate } from "react-router-dom";

export function withUserAuth(Component) {
    return (props) => {
        const { isAuthenticated, isShelter } = useContext(AuthContext);
        const navigate = useNavigate();
        useEffect(() => {
            if (!isAuthenticated) {
                navigate("/login");
            } else if (isShelter) {
                navigate("/shelter-account");
            }
        }, [isAuthenticated, isShelter, navigate]);
        return <Component {...props}/>;
    };
}
