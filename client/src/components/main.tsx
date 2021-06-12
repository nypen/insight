import React from 'react';
import { Grid, Typography } from '@material-ui/core';
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
            <Grid container spacing={2}>
                <Grid item xs={12}>
                    <AppBar />
                </Grid>
                <Grid item container direction="row">
                    <RequestForm
                        loading={loading}
                        onSubmitRequest={handleonClick}
                    />
                </Grid>
                <Grid item>
                    <pre>
                        {JSON.stringify(result, null, '\t')}
                    </pre>
                    <Typography>
                        {loading ? "true" : "false"}
                    </Typography>
                    <Typography>
                        {error ? error.message : "no error"}
                    </Typography>
                </Grid>
            </Grid>
        </div >
    );
}

export { Main }