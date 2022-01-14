class Storage {
    constructor() {
        this.storage = window.sessionStorage;
    }

    get_delimiter() {
        return this.storage.getItem('delimiter');
    }
    get_ignored_rows(){
        return this.storage.getItem('ignored_rows');
    }
    get_column_types(){
        return this.storage.getItem('column_types');
    }
    set_delimiter(delimiter) {
        return this.storage.setItem('delimiter', delimiter);
    }
    set_ignored_rows(rows){
        return this.storage.setItem('ignored_rows', rows);
    }
    set_column_types(column_types){
        return this.storage.setItem('column_types', column_types);
    }
}