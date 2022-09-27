interface Host {
    username: string;
}

export interface ThreadCard {
    name?: string | null;
    id?: number | null;
    topics?: string | null;
    sticked?: boolean | null;
    text_fill?: string | null;
    total_comments?: number | null;
    host?: Host | null;
    posted_since?: number | null;
    get_top_score?: number | null;
    user_upvote?: boolean | null;
    user_downvote?: boolean | null;
    slug?: string;
}