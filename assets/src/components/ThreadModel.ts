export interface ThreadCard {
    name: string;
    id?: number;
    dateCreated?: string;
    dateUpdated?: string;
    creator?: string;
    subForum?: string;
    sticked?: boolean;
    description?: string;
    text_fill?: string;
    numComments?: number;
}