import React from 'react';
import { Grid, LinearProgress, Typography } from '@material-ui/core';
import { AppBar } from './appBar';
import { getUrl } from '../appServices';
import { RequestFormType } from '../requestForm';
import { RequestForm } from './requestForm';

interface MainProps { }

const Main = (props: React.PropsWithChildren<MainProps>) => {

    const [error, setError] = React.useState(null);
    const [loading, setLoading] = React.useState(false);
    const [result, setResult] = React.useState(null);

    const handleonClick = (requestForm: RequestFormType) => {
        setLoading(true);

        fetch(getUrl(requestForm.id), {
            method: 'POST',
            cache: "no-cache",
            body: JSON.stringify({ username: requestForm.username, password: requestForm.password }),
            headers: new Headers({
                'mode': 'cors',
                'Content-Type': 'application/json'
            })
        })
            .then(
                (result) => {
                    console.log(result);
                    return result.json();
                },
                (error) => {
                    console.log("Error" + error);
                    setLoading(false);
                    setError(error);
                }
            )
            .then(
                (data) => {
                    setLoading(false);
                    setResult(data);
                    console.log(data)
                }
            )
    }

    return (
        <div>
            <Grid container justify="space-evenly">
                <Grid item xs={12}>
                    <AppBar />
                </Grid>
                <Grid item container xs={6}>
                    <RequestForm
                        loading={loading}
                        onSubmitRequest={handleonClick}
                    />
                </Grid>
                <Grid item xs={6}>
                    <pre>
                        {JSON.stringify(result, null, '\t')}
                    </pre>
                    {
                        loading && <LinearProgress color="secondary" />
                    }
                    <Typography color="error">
                        {error && error.message}
                    </Typography>
                </Grid>
            </Grid>
        </div >
    );
}

export { Main }