import { useNavigate, useLocation } from "react-router";


export default function LogOut() {
  const navigate = useNavigate();

  const signOut = () => {
    localStorage.removeItem("saved_token");
    navigate("/");
  };

  return (
    <>
        <button
          className="btn btn-primary btn-block"
          onClick={signOut}
        >
          Log Out
        </button>
    </>
  );
}