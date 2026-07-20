export interface DashboardStats {
    openTickets: number;
    resolvedToday: number;
    activeChats: number;
    knowledgeArticles: number;
}

export interface TicketActivity {
    day: string;
    tickets: number;
}

export interface RecentTicket {
    id: string;
    title: string;
    priority: "Low" | "Medium" | "High";
    status: "Open" | "In Progress" | "Resolved";
}

export interface ActivityItem {
    id: string;
    title: string;
    time: string;
}