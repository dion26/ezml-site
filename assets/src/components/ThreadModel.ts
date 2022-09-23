interface Host {
    username: string;
}


export interface ThreadCard {
    name: string;
    id?: number;
    topics?: string;
    sticked?: boolean;
    text_fill?: string;
    total_comments?: number;
    host?: Host;
    posted_since: number;
    get_top_score: number;
    user_upvote: boolean;
    user_downvote: boolean;
}