import { Routes, Route } from "react-router-dom";

import AppLayout from "@/app/AppLayout";

import DashboardPage from "@/features/dashboard/DashboardPage";
import ChatPage from "@/features/chat/ChatPage";
import TicketsPage from "@/features/tickets/TicketsPage";
import AnalyticsPage from "@/features/analytics/AnalyticsPage";
import KnowledgePage from "@/features/knowledge/KnowledgePage";
import SettingsPage from "@/features/settings/SettingsPage";

export default function AppRouter() {
    return (
        <Routes>
            <Route element={<AppLayout />}>
                <Route path="/" element={<DashboardPage />} />
                <Route path="/chat" element={<ChatPage />} />
                <Route path="/tickets" element={<TicketsPage />} />
                <Route path="/analytics" element={<AnalyticsPage />} />
                <Route path="/knowledge" element={<KnowledgePage />} />
                <Route path="/settings" element={<SettingsPage />} />
            </Route>
        </Routes>
    );
}