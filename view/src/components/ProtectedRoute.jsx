import React, { useContext } from "react";
import { Store } from "../context/store";
import { useNavigate, Navigate } from "react-router-dom";
import { useEffect } from "react";
import { LOGIN } from "../urls/frontend_urls";
import AccessDenied from "../pages/AccessDenied.jsx";

export default function ProtectedRoute({ children, restrict, allowedPermissions }) {
  const navigate = useNavigate();
  const { state } = useContext(Store);
  const { userInfo } = state;

  // useEffect(() => {
  //   if (!userInfo) {
  //     navigate(LOGIN);
  //   }
  // }, [navigate, userInfo]);

  return (
    userInfo?.permissions?.find(perm => allowedPermissions?.includes(perm)) || (restrict === false && userInfo)
      ? children
      : userInfo ?
        <AccessDenied />
        :
        <Navigate to={LOGIN} />
  );
}
