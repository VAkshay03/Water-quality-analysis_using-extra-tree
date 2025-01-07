import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import { QueryClient, QueryClientProvider } from "react-query";
import App from "./App";
import Predict from "./Pages/Predict";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import Result from "./Pages/Result";
import SliderPredict from "./Pages/SliderPredict";
import ParamCard from "./Components/ParamCard";
import New from "./Pages/New";
const router = createBrowserRouter([
{
path: "/",
element: <App />,
},
{
path: "/predict",
element: <New />,
},
{
path: "/result",
element: <Result />,
},
{
path: "/undesirable",
element: <Predict />,
},
{ path: "/new", element: <New /> },
]);
const queryClient = new QueryClient();
const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
<QueryClientProvider client={queryClient}>
<RouterProvider router={router} />
</QueryClientProvider>
);