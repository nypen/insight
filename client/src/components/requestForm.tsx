import React from 'react';
import { Button, FormControl, Grid, Input, InputLabel } from '@material-ui/core';
import { RequestFormType } from '../requestForm';

interface RequestFormProps { 
    loading: boolean
    onSubmitRequest: (request: RequestFormType) => void
}

const RequestForm = (props: React.PropsWithChildren<RequestFormProps>) => {
    const { loading, onSubmitRequest} = props;

    const [username, setUsername] = React.useState("");
    const [password, setPassword] = React.useState("");
    const [id, setId] = React.useState("");

    const handleonClick = () => {
        onSubmitRequest({
            id,
            username,
            password
        })
    }

    return (
        <Grid container direction="column" spacing={3}>
            <Grid item>
                <FormControl>
                    <InputLabel>Id</InputLabel>
                    <Input
                        placeholder="0ee2be67-7b4e-48a2-aad4-71dbefa7471e"
                        color="secondary"
                        value={id}
                        disabled={loading}
                        onChange={(e) => setId(e.target.value)}
                    />
                </FormControl>
            </Grid>
            <Grid item>
                <FormControl>
                    <InputLabel>Username</InputLabel>
                    <Input
                        color="secondary"
                        value={username}
                        disabled={loading}
                        onChange={(e) => setUsername(e.target.value)}
                    />
                </FormControl>
            </Grid>
            <Grid item>
                <FormControl>
                    <InputLabel>Password</InputLabel>
                    <Input
                        color="secondary"
                        value={password}
                        disabled={loading}
                        onChange={(e) => setPassword(e.target.value)}
                    />
                </FormControl>
            </Grid>
            <Grid item>
                <Button
                    onClick={handleonClick}
                    disabled={loading}
                >
                    Produce JsonLD
                </Button>
            </Grid>
        </Grid>
    );
}

export { RequestForm }